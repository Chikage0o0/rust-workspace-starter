FROM rust:alpine AS chef

RUN apk add --no-cache \
    build-base \
    musl-dev \
    openssl-dev \
    pkgconfig
COPY rust-toolchain.toml rust-toolchain.toml
RUN cargo --version && rustc --version
RUN cargo install cargo-chef --locked

WORKDIR /app

FROM chef AS planner
COPY . .
RUN cargo chef prepare --recipe-path recipe.json

FROM chef AS builder
COPY --from=planner /app/recipe.json recipe.json
RUN cargo chef cook --release --recipe-path recipe.json
COPY . .
RUN cargo build --release --bin app

FROM alpine:latest AS runtime
ENV TZ=Asia/Shanghai
RUN apk add --no-cache ca-certificates tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

RUN addgroup -S app && adduser -S -G app app
WORKDIR /app

COPY --from=builder /app/target/release/app /usr/local/bin/app

USER app
ENTRYPOINT ["app"]

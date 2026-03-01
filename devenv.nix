{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  env.OPENSSL_LIB_DIR = "${pkgs.pkgsStatic.openssl.out}/lib";
  env.OPENSSL_INCLUDE_DIR = "${pkgs.pkgsStatic.openssl.dev}/include";
  env.OPENSSL_STATIC = 1;
  env.OPENSSL_NO_VENDOR = 1;
  env.PKG_CONFIG_ALL_STATIC = 1;

  dotenv.enable = true;

  enterShell = ''
    if [ -d .git ] && command -v pre-commit >/dev/null 2>&1; then
      # 自动安装 pre-commit hook，重复执行是幂等的。
      pre-commit install --install-hooks --hook-type pre-commit >/dev/null
    fi
  '';

  packages = [
    pkgs.git
    pkgs.nixfmt
    pkgs.pkgsStatic.openssl
    pkgs.pkg-config

    # 开发工具
    pkgs.tokei
    pkgs.ripgrep
    pkgs.pre-commit
    pkgs.cargo-audit
    pkgs.cargo-outdated
    pkgs.cargo-nextest
  ];

  languages.rust = {
    enable = true;
    toolchainFile = ./rust-toolchain.toml;
  };

  languages.python = {
    enable = true;
  };
}

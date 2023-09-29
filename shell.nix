{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    poetry
    python311
    docker
    docker-compose
    flyctl
  ];

  shellHook = ''
    poetry env use python3.11
    poetry install
    if [ -z $DOCKER_HOST ]
    then
      echo 'Missing DOCKER_HOST environment variable'
      export DOCKER_HOST='unix:///tmp/podman.sock'
      if [ ! -S /tmp/podman.sock ]
      then
        echo 'Spawning podman process'
        ${pkgs.podman}/bin/podman system service --time=0 $DOCKER_HOST &
      fi
    fi
  '';
}

{
  description = "Baitless: Offline youtube interface.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };
  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux"; # Adjust if needed
      pkgs = import nixpkgs { inherit system; };
      python = pkgs.python3.override {
        packageOverrides = new: old: {
        };
      };
    in
    {
      devShells.${system}.default = pkgs.mkShell rec {
        buildInputs = with pkgs; [
          (python.withPackages (
            ps: with ps; [
              yt-dlp
              cx-freeze
              qrcode
              flask
              pillow
              opencv-python
              fpdf2
              pypdf
            ]
          ))
        ];

        shellHook = ''
          # Add necessary paths for dynamic linking
          export LD_LIBRARY_PATH=${
            pkgs.lib.makeLibraryPath (
              [
                "/run/opengl-driver" # Needed to find libGL.so
              ]
              ++ buildInputs
            )
          }:$LD_LIBRARY_PATH
        '';
      };
    };
}

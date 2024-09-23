# shell.nix
{ pkgs ? import <nixpkgs>{} }:
  let 
    pythonPackages = pkgs.python312Packages;
  in
  pkgs.mkShell {
  buildInputs = (with pythonPackages; [
    python 
    numpy
    scipy
    scikit-learn
    matplotlib
    pandas
	openpyxl
  ]);
}

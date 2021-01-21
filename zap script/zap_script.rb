#!/usr/bin/env ruby

file = File.read('casks.txt').split
j=0;
for i in file
  if j==5
    break
  end
  system("brew install --cask %{i}" % {:i => i })
  require "%{i}" % {:i => i }
  system("open -a %{i}" % {:i => i })
  system("brew cask createzap %{i}" % {:i => i })
  system("brew uninstall --cask %{i}" % {:i => i })
  j += 1
end
# Homebrew-cask-bump

The BumpIt script makes use of `brew livecheck` and `brew bump-cask-pr` to check for new version of casks and PR the version bumps to Homebrew Cask repo.

Warning: The script may take a long time to complete execution.

## Usage

Run the script using

```bash
python3 BumpIt.py
```

This will print the bump-pr statements to the terminal which can be run by simply pasting back into the terminal.

If you want to write these outputs to a bash script instead and execute use

```bash
python3 BumpIt.py > <filename>.sh
bash <filename>.sh
```

Although it is possible to directly send the PRs from within the BumpIt script(simply uncomment the last line in the script), it is reccomended that you print to terminal or file and examine before executing as livecheck might sometimees return versions that are unstable releases or pre-releases.


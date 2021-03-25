# jsort
watch for new files in the downloads folder, and sort accordingly

## Requirements

- Python requirements can be found in the [`pyproject.toml`](https://github.com/sudo-julia/file-sorter/blob/main/pyproject.toml)

- Optionally, install `libyaml` as seen [here](https://github.com/gorakhargosh/watchdog#installation-caveats)
to speed up `watchdog`'s PyYAML parser

## TODO

- [ ] Add a config file to override the dirs automatically detected by `set_dirs.py`
- [ ] Add support to run [`fawkes`](https://github.com/Shawn-Shan/fawkes) on images

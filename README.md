## VintageousPlus (DEPRECATED)
[![Build Status](https://travis-ci.org/trishume/VintageousPlus.svg?branch=master)](https://travis-ci.org/trishume/VintageousPlus)

### VintageousPlus has merged into [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous) in collaboration with @gerardroche

**VintageousPlus** is a fork of the awesome [Vintageous](https://github.com/guillermooo/Vintageous) plugin for Sublime Text 3. The original author [@guillermooo](https://github.com/guillermooo) doesn't seem to be maintaining it anymore, so this fork steps up to merge outstanding PRs and add some new features.

### Changes from Vintageous

One major change that isn't a code change is that if you submit PRs, I will review them and likely merge them. **Please help me make Vintageous better!**

#### New stuff

- [@guillermooo's surround.vim plugin for Vintageous](https://github.com/guillermooo/Vintageous_Plugin_Surround) has been integrated and enabled by default behind a setting.
- Added the ability to enable/disable bindings via a setting. Now you can PR your fancy extra functionality into this repo and have it be easy for users to enable/disable.

#### Fixes some minor bugs

- `c_` and `d_` no longer cause an error

#### The following outstanding PRs have been merged

- [Add Support for Sublime Wrap Plus](https://github.com/guillermooo/Vintageous/pull/1077)
- [Fix interactive commands not working after mapped commands](https://github.com/guillermooo/Vintageous/pull/1042)
- [Fix for P newline pasting](https://github.com/guillermooo/Vintageous/pull/1041)
- [Settings, Menus, Run tests keymaps](https://github.com/guillermooo/Vintageous/pull/1030)
- [New text objects](https://github.com/guillermooo/Vintageous/pull/1074)

### Installing

**Make sure that Vintage
is in the `ignored_packages` list
in your user preferences.**

You can install VintageousPlus in multiple ways:

##### Building from Source

1. Clone this repository
2. Optionally, update to a specific tag
3. Run `./bin/build.sh` (OS X/Linux) or `bin/Publish.ps1` (Windows).

Refer to the [wiki](https://github.com/guillermooo/Vintageous/wiki) for more information.

### Settings

See [VintageousPlus/Preferences.sublime-settings](https://github.com/trishume/VintageousPlus/blob/master/Preferences.sublime-settings) for a comprehensive list of settings.

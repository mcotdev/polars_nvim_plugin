# polars_nvim_plugin
## NeoVim Plugin for Polars

Work in progress to build a NeoVim or Vim plugin for Polars

Configure Neovim to use the plugin: Add your plugin's path to the rtp (runtimepath) in your Neovim configuration file (e.g., ~/.config/nvim/init.vim or ~/.vimrc). Replace `/path/to/polars_nvim_plugin` with the actual path to your plugin directory:

`set rtp+=/path/to/polars_nvim_plugin`

Test the plugin: Open Neovim and run the :UpdateRemotePlugins command to register your plugin. 

Restart Neovim, and you can now use the :call PolarsShowFirstRows(file_path, num_rows) command to show the first num_rows rows of the CSV file at file_path. 

For example:

`:call PolarsShowFirstRows('/path/to/data.csv', 5)`

This will display the first 5 rows of the CSV file in Neovim's output.

import pynvim
import polars as pl

@pynvim.plugin
class PolarsPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function("PolarsShowFirstRows")
    def polars_show_first_rows(self, args):
        file_path = args[0]
        num_rows = int(args[1]) if len(args) > 1 else 10

        try:
            df = pl.read_csv(file_path)
            first_rows = df.head(num_rows)
            self.nvim.out_write(str(first_rows))
        except Exception as e:
            self.nvim.err_write(f"Error: {str(e)}\n")

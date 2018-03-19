# from bokeh.plotting import figure, show
from itertools import count

from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, DataRange1d, Grid, LinearAxis, Plot
from bokeh.models.glyphs import Arc, Quadratic
from bokeh.palettes import Plasma256, Viridis256


def jumper(instructions):
    status = instructions
    LO, HI = 0, len(status)
    index = 0
    while(LO <= index < HI):
        jump_n = status[index]
        status[index] += 1
        index += jump_n
        yield index


def plotjumps(jumps, ninstructions):
    xs = [0] + jumps[:-1]
    ys = [0 for _ in jumps]
    rs = [abs(x1-x0)/2 for x0, x1 in zip(xs, jumps)]
    xs = [x+r for x, r in zip(xs, rs)]
    colors = [Plasma256[255-round(i * 255/len(jumps))]
              for i, _ in zip(count(0), jumps)]

    source = ColumnDataSource(
        dict(x=xs, y=ys, r=rs, c=colors))

    xdr = DataRange1d(start=0, end=ninstructions+0.25)
    ydr = DataRange1d(start=0)

    plot = Plot(
        title=None, x_range=xdr, y_range=ydr, plot_width=800, plot_height=800,
        h_symmetry=False, v_symmetry=False, min_border=0)  # , toolbar_location=None)

    glyph = Arc(x="x", y="y", radius="r", start_angle=0,
                end_angle=3.10, line_alpha=1, line_color="c")

    plot.add_glyph(source, glyph)

    xaxis = LinearAxis()
    plot.add_layout(xaxis, 'below')

    yaxis = LinearAxis()
    plot.add_layout(yaxis, 'left')

    plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
    plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

    curdoc().add_root(plot)

    show(plot)


if __name__ == "__main__":
    TESTCASES = [([0, 3, 0, 1, -3], 5)]

    for instructions, expected in TESTCASES:
        result = list(jumper(instructions))
        assert(len(result) == expected)

    plotjumps(result, 5)

    PUZZLEFILENAME = '.\\2017\\day05\\input.txt'
    with open(PUZZLEFILENAME) as infile:
        instructions = [int(x) for x in infile.readlines()]

    result = list(jumper(instructions))
    # print(result)

    plotjumps(result, len(instructions))

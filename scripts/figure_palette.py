"""Shared ink, accent and paper colors for the survey's vector figures."""
NAVY = '#17324D'
BLUE = '#275D9F'
TEAL = '#007A72'
RED = '#B4493B'
AMBER = '#996300'
SLATE = '#52677E'
MUTED = '#5B6876'
BLUE_FILL = '#E2EBF4'
TEAL_FILL = '#DBEEE7'
RED_FILL = '#F3E1DA'
AMBER_FILL = '#F3E9D2'
SLATE_FILL = '#E5ECF1'
RULE = '#DCE3EA'


def configure_figure_fonts():
    """Use clear sans-serif labels and embed scalable TrueType text in PDFs."""
    import matplotlib as mpl
    mpl.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Segoe UI', 'Arial', 'Liberation Sans', 'DejaVu Sans'],
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
        'svg.fonttype': 'none',
        'text.color': NAVY,
        'axes.unicode_minus': False,
    })

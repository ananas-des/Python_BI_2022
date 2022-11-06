#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import ConnectionPatch
import matplotlib.colors as mcolors


def read_gff(gff_file):
    '''Function read_gff() reads either gziped or not .gff file and transforms it into pandas.DataFrame
    
    Parameters:
    gff_file (str): path to .gff input file
    
    Returns: pandas.DataFrame 
    '''
    
    df_gff = pd.read_table(gff_file, sep='\t', skiprows=1, names=['chromosome', 'source', 'type', 'start', 
                                                                  'end', 'score', 'strand', 'phase', 'rRNA_type'])
    df_gff["rRNA_type"] = df_gff["rRNA_type"].str.extract('(\d{1,2}S)') # extracting type of rRNA from string
    return df_gff


def read_bed6(bed_file):
    '''Function read_bed() reads .bed file and transforms it into pandas.DataFrame
    
    Parameters:
    bed_file (str): path to .bed input file
    
    Returns: pandas.DataFrame 
    '''
    
    df_bed = pd.read_table(bed_file, sep='\t', names=['chromosome', 'start', 'end', 
                                                      'name', 'score', 'strand'])
    return df_bed


df_annot = read_gff("rrna_annotation.gff")

df_aln = read_bed6("alignment.bed")

# DataFrame with the number of sequences in rRNA types for each reference 
rRNA_type_chr =  df_annot.groupby('chromosome')['rRNA_type'].value_counts().unstack().fillna(0)
rRNA_type_chr

# bar plot for rRNA_type_chr
plt.rcParams["figure.dpi"] = 300
rRNA_type_chr.plot(kind='bar', xlabel='Sequence', ylabel='Count', 
                   fontsize=9, figsize=(12, 6))

# DataFrame with contigs ('name' column) that covers reference rRNA
intersection_df = pd.merge(df_annot, df_aln, on='chromosome', how='inner') # merging two DataFrames on 'chromosome'

# filtering contigs that and references that intersect
intersection_df = intersection_df[(intersection_df.start_y < intersection_df.start_x)
                                  & (intersection_df.end_x <= intersection_df.end_y)]

# reading .tsv.gz file with differetial expression data
diffexp_data = pd.read_table("diffexpr_data.tsv.gz", sep='\t')

def exp_changes(row):
    '''Function exp_changes() compares log_pval and logFC from diffexpr_data.tsv.gz 
    with threads and sets expression class for each gene
    - thread for log_pval = -log(0.05) = 1.301, where p-value=0.05
    - thread for logFC = 0 (gene is not differentially expressed)
    
    Parameteres:
    row (numpy.Series): DataFrame row - information about gene expression
    
    Returns: class for each gene
    1) 'Significantly downregulated' - log_pval >= 1.301 and logFC < 0;
    2) 'Significantly upregulated' -  log_pval >= 1.301 and logFC > 0;
    3) 'Non-significantly downregulated' - log_pval < 1.301 and logFC < 0;
    4) 'Non-significantly upregulated' - log_pval < 1.301 and logFC > 0  
    '''
    
    if row.log_pval >= 1.301 and row.logFC < 0:
        return 'Significantly downregulated'
    if row.log_pval >= 1.301 and row.logFC > 0:
        return 'Significantly upregulated'    
    if row.log_pval < 1.301 and row.logFC < 0:
        return 'Non-significantly downregulated'
    if row.log_pval < 1.301 and row.logFC > 0:
        return 'Non-significantly upregulated'


# adding new column with gene expression class    
diffexp_data['changes'] = diffexp_data.apply (lambda row: exp_changes(row), axis=1)

# DataFrame with two the most significantly down- and upregulated genes
sig_exp = diffexp_data[diffexp_data.changes.str.contains(
    'Significantly', regex=True, na=False)].sort_values(
    by='logFC', ascending=False).iloc[[0,1,-2,-1]]

# grouping order for hue and legend
hue_order = [
    'Significantly downregulated', 'Significantly upregulated', 
    'Non-significantly downregulated', 'Non-significantly upregulated'
]

# figure size and resolution
plt.figure(figsize=(12,6), dpi=300)

#scatter plot using seaborn
volcano_plot = sns.scatterplot(
    data=diffexp_data, x='logFC', y='log_pval',
    hue='changes', hue_order=hue_order, s=10, linewidth=0
)

# vertical line (x=0)
plt.axvline(0, color='grey', linestyle='--', linewidth=1)
# horizontal line (y=1.301)
plt.axhline(1.301, color='grey', linestyle='--', linewidth=1)
# limits for x axis
plt.xlim([min(diffexp_data.logFC)-1, max(diffexp_data.logFC)+1.5])

# legend customization without title
volcano_plot.legend(
    title=None, shadow=True, 
    fontsize=10, markerscale=1.5, prop={'weight' : 'bold'}
)

# show minor ticks
plt.minorticks_on()
# ticks and tick labels cutomization
plt.tick_params(direction='out', labelsize=10, length=6, width=1)
volcano_plot.set_yticklabels(volcano_plot.get_yticks(), weight='bold')
volcano_plot.set_xticklabels(volcano_plot.get_xticks(), weight='bold')

# plot title
plt.title('Volcano plot', size=24, fontweight='bold', style='italic')
# x and y labels with underscored log bases
plt.xlabel(
    'log$_{\mathbf{2}}$(fold change)', size=16, 
    fontweight='bold', style='italic'
)
plt.ylabel(
    '-log$_{\mathbf{10}}$(p value corrected)', size=16, 
    fontweight='bold', style='italic'
)

# text near horizontal line
plt.text(8, 2, 'p value = 0.05', color='grey', size=10, fontweight='bold')

# adding annotation for two the most 
# significantly down- and upregulated genes
for index, row in sig_exp.iterrows():
    plt.annotate(
        row.Sample, xy=(row.logFC, row.log_pval),
        fontweight='bold',
        xytext=(row.logFC+0.25, row.log_pval+15),
        horizontalalignment='right',
        arrowprops=dict(
            facecolor='red', edgecolor='black',
            width=3, headwidth=7
        )
    )
    
# importing Top 100 Languages data
data = pd.read_csv("Top_100_Languages.csv", skiprows=1,
                          names=['Language', 'Total_Speakers',
                                 'Native_Speakers', 'Origin'], decimal=',').drop(
    columns=['Total_Speakers','Origin']).set_index('Language')

data.Native_Speakers=data.Native_Speakers.replace(np.nan, 0).astype('int')

# Splitting data
cutoff = 80000000
df1 = data[data.Native_Speakers > cutoff].sort_values(
    by='Native_Speakers', ascending=False) # sorted top wedges
others_df = data[data.Native_Speakers <= cutoff].sort_values(
    by='Native_Speakers', ascending=True) # bottom wedges
df2 = others_df.sum().rename({'Native_Speakers':'Others'}).to_frame(
    name='Native_Speakers') # summed bottom wedges
df3 = pd.concat([df1, df2]) #combined DataFrame

def calc_coords(wedges, delt = 0.2, x_mul=1.3):
    '''Fuction calc_coords() generates coords for drawing arrows and text boxes'''
    
    angs, xs, ys = [], [], []
    for wedge in wedges:
        ang = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        angs.append(ang)
        xs.append(x)
        ys.append(y)
        
    nys = ys.copy()
    for i in range(1,len(ys)-1):
        if np.sign(xs[i]) != np.sign(xs[i-1]):
            nys[i] = nys[i-1]
        elif nys[i-1] - nys[i] < delt and xs[i] <= 0:
            nys[i] = nys[i-1] - delt
        elif nys[i-1] - nys[i] <xs[i] > 0:
            nys[i] = nys[i-1] + delt
    nxs = [x_mul * np.sign(i) for i in xs]
    return angs, [*zip(xs,ys)], [*zip(nxs, nys)]



shares = df3['Native_Speakers'] / df3['Native_Speakers'].sum()
explode = [i/10 for i in shares]
# Generate subplots
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(12, 6),  dpi=300,
    gridspec_kw={'width_ratios': [5, 2]}
)

# subplot 1 is the piechart itself
wedges, texts = ax1.pie(
    df3.Native_Speakers, explode=explode, startangle=180* shares[-1], 
    colors=sns.color_palette("Set2", n_colors=13)
)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(
    arrowprops=dict(arrowstyle="-"), bbox=bbox_props, 
    zorder=0, va="center", fontsize = 8
)

# Calculation of coords for labels
# Alter param::delt to change spacing between clumped boxes
angs, coords, txt_coords = calc_coords(wedges)

# Drawing arrows and text boxes
for i, wedge in enumerate(wedges):
    connectionstyle = "angle,angleA=0,angleB={}".format(angs[i])
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax1.annotate(
        df3.index[i]+f'\n{shares[i]:.2%}',
        xy=coords[i], xytext=txt_coords[i],
        horizontalalignment='center', **kw)
    
ax1.set_title("Top 100 languages by Native Speakers", fontsize=14, fontweight='bold')

# Draw stacked bar plot with annotations
bottom = 1
width = .2
bar_palette = sns.color_palette("Paired", n_colors=100)

for i, (index, row) in enumerate(others_df.iterrows()):
    height = row['Native_Speakers']/others_df['Native_Speakers'].sum()
    bottom -= height
    bc = ax2.bar(
        0, height, width, bottom=bottom, 
        label=index, color=bar_palette[i]
    )
    if height > 0.02:
        ax2.annotate(
            f"{height:.1%}", xy=(width, bottom), 
            fontsize=(height * 300)
        )

ax2.set_title('Bottom of the Top-100', fontsize=12, fontweight='bold')
ax2.axis('off')
ax2.set_xlim(-width, 5 * width)

# use ConnectionPatch to draw lines between the two plots
thetas = wedges[-1].theta1, wedges[-1].theta2
center, r = wedges[-1].center, wedges[-1].r

# drawing connecting lines
for i in [0,1]:
    x = r * np.cos(np.pi / 180 * thetas[i]) + center[0]
    y = r * np.sin(np.pi / 180 * thetas[i]) + center[1]
    con = ConnectionPatch(
        xyA=(-width / 2, i), coordsA=ax2.transData,
        xyB=(x, y), coordsB=ax1.transData
    )
    con.set_color([0, 0, 0])
    con.set_linewidth(0.7)
    ax2.add_artist(con)


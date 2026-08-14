# honesty: rules that override any choice

Generated from the Open Visualization Protocol v1.1 canon. Do not edit; edit the canon and rebuild.

## Always

- Bars and columns always start at zero. Never truncate a value axis.
- Pie or donut only for a part-to-whole with 3 slices or fewer; otherwise rank the categories.
- Never a second Y axis. Use two stacked panels or an indexed line rebased to 100.
- Direct-label the marks; reach for a legend only when direct labels will not fit.
- One message per chart. If it needs two, make two charts.
- Sort by the value, not the alphabet, unless the order carries meaning (time, size class, process step).
- Every chart states its source and, where a total is implied, reconciles it in the title.
- No 3D, no exploded slices, no decorative gradients. Ink serves the data or it goes.

## Per-chart cautions

Charts that carry their own warnings. Honor these before using them.

| Chart | Never |
|---|---|
| SCATTER (CH-COR-01) | trend lines without stating the fit (no silent regressions); color-coded groups without direct labels; log scales without declaring them |
| BUBBLE (CH-COR-02) | radius-proportional sizing (quadruples the visual weight); size legends with sample circles; overlapping unlabeled bubble clouds |
| XY HEATMAP (CH-COR-03) | rainbow color scales; cells without printed values; sorting an ordered dimension by value |
| COLUMN + LINE (CH-COR-04) | unlabeled dual axes; non-zero baselines on either scale; three or more scales |
| HEXBIN (CH-COR-05) | rainbow density ramps; smoothed density contours sold as data; hexbins for tiny datasets |
| PARALLEL COORDINATES (CH-COR-06) | WARN ENTRY: crossings between axes are artifacts of axis order, not relationships; analysts only; min-max normalization hiding the zero; more than 12 lines |
| SCATTERPLOT MATRIX (CH-COR-07) | WARN ENTRY: a SPLOM is a workbench, not a deliverable; ship CH-COR-01 of the pair that matters; gridlines and ticks in mini cells; 4+ variables |
| DIVERGING BAR (CH-DEV-01) | color without signed labels (color-blind readers lose the sign); asymmetric scales that exaggerate one side; sorting alphabetically |
| DUMBBELL (CH-DEV-02) | arrows instead of connectors (double-encodes direction); legends; sorting that hides the counter-mover |
| SPINE (CH-DEV-03) | three or more segments; legends; rows normalized to different totals without saying so |
| SURPLUS/DEFICIT AREA (CH-DEV-04) | asymmetric y ranges that shrink one sign; using it when the series never changes sign; gradient fills |
| DIVERGING STACKED (CH-DEV-05) | rainbow level palettes; a neutral level hidden inside a side; per-level value labels squeezed into segments |
| HISTOGRAM (CH-DST-01) | gaps between bars; unequal bins without width-proportional areas; labeling bin centers |
| DOT PLOT (CH-DST-02) | legends; different scales per row; more than two dots per row |
| DOT STRIP (CH-DST-03) | random jitter (breaks determinism and honesty); per-row scales; summarizing away the raw values |
| BOXPLOT (CH-DST-04) | mixing whisker conventions across rows; boxplots for general audiences without a reading key; hiding sample sizes |
| POPULATION PYRAMID (CH-DST-05) | different scales per side (the classic pyramid lie); unordered bands; more than two sides |
| CUMULATIVE CURVE (CH-DST-06) | cumulative curves that end below 100 without saying why; reading the curve as a trend over time (thresholds are not time) |
| BEESWARM (CH-DST-07) | random jitter; labeling every dot; sized dots (use CH-COR-02) |
| VIOLIN (CH-DST-08) | violins for general audiences; silent KDE with hidden bandwidth; per-row normalization sold as comparable |
| DENSITY CURVE (CH-DST-09) | overlapping filled densities; silent KDE with hidden bandwidth; reading the y axis as counts |
| ERROR BARS (CH-DST-10) | error bars without saying what they represent; bars with whiskers (length + interval double-encodes); hiding uncertainty to look confident |
| WATERFALL (CH-FLO-01) | supplying the end total as data (it must reconcile by construction); unsigned delta labels; sorting steps by size (a bridge is a narrative, keep the told order) |
| SANKEY (CH-FLO-02) | links whose widths change between ends; crossing minimization by randomization; cycles |
| NETWORK (CH-FLO-03) | force-directed or random layouts; unlabeled nodes; edge crossings read as meaning |
| CHORD (CH-FLO-04) | WARN ENTRY: chord diagrams decorate; CH-TAB-02 or a sankey informs; self-loops; more than 6 nodes |
| COLUMN (CH-MAG-01) | sorting by value when order is natural (that chart is CH-RNK-01); value axis plus direct labels (pick direct labels); rainbow columns |
| PAIRED COLUMN (CH-MAG-02) | three or more series per group; legends; truncated baseline |
| PAIRED BAR (CH-MAG-03) | legends; two different scales; sorting away a natural order |
| BULLET (CH-MAG-04) | gauges (this IS the honest gauge); rainbow bands; missing target |
| PROPORTIONAL SYMBOL (CH-MAG-05) | radius-proportional scaling (the classic double-count lie); unprinted values; more than 7 symbols |
| PICTOGRAM (CH-MAG-06) | icons whose area distorts the count; undeclared unit value; different unit values per row |
| RADAR (CH-MAG-07) | WARN ENTRY: radars are usually the wrong answer; paired bars read faster and more honestly; mixed units across axes; 3+ series |
| PARLIAMENT (CH-MAG-08) | rainbow party palettes; non-integer seat counts; using it for shares that are not allocations |
| GAUGE (CH-MAG-09) | WARN ENTRY: a gauge spends maximal ink on one number; CH-MAG-04 shows five in the same space; unlabeled bands; 3D dials |
| STACKED BAR (CH-PTW-01) | legend boxes; more than 4 segments; stacking non-additive measures |
| STACKED BAR 100% (CH-PTW-02) | using 100% stacked when totals shrink (it hides decline); legend boxes; labeling every segment share (label the key segment only) |
| PIE (CH-PTW-03) | more than 3 slices; 3D or exploded slices; legends |
| DONUT (CH-PTW-04) | more than 3 slices (the classic dashboard donut crime); KPI number stuffed in the hole while the ring shows something else; thin progress rings pretending to be charts |
| TREEMAP (CH-PTW-05) | rainbow cells (one hue plus one highlight, always); labels crammed into tiny cells; nested hierarchies in this entry |
| WAFFLE (CH-PTW-06) | icon waffles (pictogram people); multi-color waffles; partial cells |
| MARIMEKKO (CH-PTW-07) | more than 6x4 cells; legends; 3D mosaic effects |
| FUNNEL (CH-PTW-08) | funnel shapes with slanted sides (fake geometry); increasing stages; more than 6 stages |
| SUNBURST (CH-PTW-09) | WARN ENTRY: a treemap (CH-PTW-05) answers the same question with readable areas; 3+ rings; rainbow slices |
| CIRCLE PACK (CH-PTW-10) | WARN ENTRY: circle areas are the least readable encoding that still counts as a chart; CH-PTW-05 whenever anyone must compare; random or physics layouts; nesting deeper than one level |
| BAR-H (CH-RNK-01) | value axis plus direct labels (pick direct labels); one color per bar (rainbow bars); 3D depth or shadows on bars |
| ORDERED COLUMN (CH-RNK-02) | unsorted ranking; truncated baseline; rainbow columns |
| LOLLIPOP (CH-RNK-03) | dots without sticks (loses the zero anchor); truncated baseline |
| BUMP (CH-RNK-04) | plotting values on the bump y axis; more than 8 series; legends |
| DOT STRIP (CH-RNK-05) | dot strips for unbounded scales without stating the scale; gridline clutter |
| TABLE WITH BARS (CH-RNK-06) | zebra striping; unsorted rows; sparklines squeezed into cells |
| CHOROPLETH (CH-SPA-01) | rainbow choropleths; absolute counts on area fills; unlabeled regions |
| PROPORTIONAL SYMBOL MAP (CH-SPA-02) | radius scaling; colored base regions competing with symbols; unlabeled symbols |
| ROUTE PROGRESS (CH-SPA-03) | progress percentages that are not length-true; decorating with terrain; more than ~8 stations |
| DOT DENSITY (CH-SPA-04) | renderer-side random scatter (breaks determinism); reading individual dots as items; undeclared dot value |
| FLOW MAP (CH-SPA-05) | two-way arrows on one curve; more than 8 flows; width not proportional to value |
| STATUS MATRIX (CH-TAB-01) | color-only status dots; zebra striping; sorting rows by health (readers lose their row) |
| HEATMAP TABLE (CH-TAB-02) | red-green judgment coloring on magnitude data; global normalization across mixed units; cells without printed values |
| KPI TABLE (CH-TAB-03) | zebra striping; coloring deltas by sign when down is good; reading trend cells against each other |
| LINE (CH-TIM-01) | legend boxes; more than one saturated series; dual y axes |
| S-CURVE (CH-TIM-02) | legend boxes; truncated y axis to flatter progress; plotting period values and calling it an S-curve |
| AREA (CH-TIM-03) | multiple overlapping filled areas; area for rates or percentages; truncated baseline |
| STACKED AREA (CH-TIM-04) | more than 4 bands; legends; reading middle bands as levels |
| SLOPE (CH-TIM-05) | more than 7 lines; legends; curved connectors |
| SPARKLINE STRIP (CH-TIM-06) | shared scale implied across rows; axes or gridlines on sparklines; coloring deltas by sign when down is good |
| CALENDAR HEATMAP (CH-TIM-07) | sorting weekdays by value; rainbow ramps; cells without values |
| FAN (CH-TIM-08) | bands without a named method; solid median implying certainty; hiding the actual/forecast boundary |
| GANTT (CH-TIM-09) | rainbow bars per task; fake dependency arrows crisscrossing; percent labels on every bar (the overlay shows it) |
| CONNECTED SCATTER (CH-TIM-10) | arrows on every segment; smoothing the trail; unlabeled periods |
| STREAMGRAPH (CH-TIM-11) | WARN ENTRY: streamgraphs cannot be read, only admired; CH-TIM-04 for any real question; y axes on a wandering baseline; legends |
| HORIZON (CH-TIM-12) | WARN ENTRY: horizons are for trained monitoring eyes; anyone else needs CH-TIM-06; per-row scales sold as comparable; reading values off folds |
| STEP (CH-TIM-13) | smooth or diagonal interpolation of held values (invents data); markers on every step; legends |
| INDEXED LINE (CH-TIM-14) | indexing series that share a unit (hides real gaps); hiding the base period; reading index points as percent without saying so (132 = +32%) |
| EVENT TIMELINE (CH-TIM-15) | curved journey arrows; icons instead of markers; more than 8 events on one axis |

Built on the Open Visualization Protocol (https://github.com/babarda/open-visualization-protocol).

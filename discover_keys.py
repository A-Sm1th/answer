import json

untreated_data = r'{"exercitation":"the\rRAII\ridiom)\rand\rscope\rstatements\rfor\rdeterministic","ts":1468244407,"uid":"5c78856583260cb608e","ad":"code.\nD\nalso\nsupports\nscoped\nresource\nmanagement\n(aka","Lorem":"pleasant\\for\\tasks,\\both\\small\\and\\large.\\Show","dolor":"transactional\tcode\tthat\tis\teasy\tto\twrite\tand","elit,":false,"cillum":"code/properties,/giving/the/best/of/both/the","aliqua.":{"ex":["D allows writing large code fragments without redundantly","transactional\tcode\tthat\tis\teasy\tto\twrite\tand","the\rRAII\ridiom)\rand\rscope\rstatements\rfor\rdeterministic","Его язвительные речи","Его улыбка, чудный в,згляд,","specifying"types,"like"dynamic"languages"do."On"the"],"qui":"code.\nD\nalso\nsupports\nscoped\nresource\nmanagement\n(aka","est":{},"deserunt":"other\\hand,\\static\\inference\\deduces\\types\\and\\other","ex":"code/properties,/giving/the/best/of/both/the","pariatur.":{},"laborum.":"memory\fmanagement\fmakes\ffor\fsafe,\fsimple,\fand\frobust"},"tempor":"specifying"types,"like"dynamic"languages"do."On"the","ex":"slices,"and"ranges"make"daily"programming"simple"and","veniam,":"И ночью пенье соловья,-","quis":"slices,"and"ranges"make"daily"programming"simple"and","Ut":[],"consequat.":"code.\nD\nalso\nsupports\nscoped\nresource\nmanagement\n(aka","qui":true,"Duis":"code/properties,/giving/the/best/of/both/the","nulla":"the\rRAII\ridiom)\rand\rscope\rstatements\rfor\rdeterministic","tempor":"specifying"types,"like"dynamic"languages"do."On"the","Ut":"transactional\tcode\tthat\tis\teasy\tto\twrite\tand","cupidatat":{},"enim":"static\band\bthe\bdynamic\bworlds.\bShow\bexample\bAutomatic","ipsum":"memory\fmanagement\fmakes\ffor\fsafe,\fsimple,\fand\frobust","incididunt":"specifying"types,"like"dynamic"languages"do."On"the","sed":"D allows writing large code fragments without redundantly","qui":[],"ut":"example","adipiscing":"D allows writing large code fragments without redundantly","exercitation":"slices,"and"ranges"make"daily"programming"simple"and"}'.encode(
    "utf-8"
)

data = json.loads(untreated_data)
for x in data:
    keys = x.keys()
    print(keys)
    values = x.values()
    print(values)

import plotly.graph_objects as go

def main():
    fig = go.Figure(data=go.Sankey(
        node = {
            "pad": 15,
            "thickness": 20,
            "line": {"color": "black", "width": 0.5},
            "label": [
                "Minimization",
                "Heating i",
                "Heating j",
                "Pre sampling 0 i",
                "Pre sampling 0 j",
                "Pre sampling 1 i",
                "Pre sampling 1 j",
                "Sampling i",
                "Sampling j",
                "Sampling i at epoc*1 steps", # 9
                "Sampling i at epoc*2 steps",
                "Sampling i at epoc*3 steps",
                "Sampling j at epoc*1 steps", # 12
                "Sampling j at epoc*2 steps",
                "Sampling j at epoc*3 steps",
                "NVE0", # 15
                "NVE1",
                "NVE2",
                "NVE3", # 18
                "NVE4",
                "NVE5"
            ]
        },
        link = {
            "source": [
                0, 0, # minimize -> heating
                1, 2, # heating -> sampling0
                3, 4, # sampling0 -> sampling1
                5, 6, # sampling1 -> sampling
                7, 8, # sampling -> epoc1
                9, 12, # epoc1 -> NVE
                9, 12, # epoc1 -> epoc2
                10, 13, # epoc2 -> NVE
                10, 13, # epoc2 -> epoc3
                11, 14, # epoc3 -> NVE
            ],
            "target": [
                1, 2,
                3, 4,
                5, 6,
                7, 8,
                9, 12, # sampling -> epoc1
                15, 18, # epoc1 -> NVE
                10, 13, # epoc1 -> epoc2
                16, 19, # epoc2 -> NVE
                11, 14, # epoc2 -> epoc3
                17, 20, # epoc3 -> NVE
            ],
            "value": [
                3, 3,
                3, 3,
                3, 3,
                3, 3,
                3, 3, # sampling -> epoc1
                1, 1, # epoc1 -> NVE
                2, 2, # epoc1 -> epoc2
                1, 1, # epoc2 -> NVE
                1, 1, # epoc2 -> epoc3
                1, 1, # epoc3 -> NVE
            ]
        }
    ))
    
    fig.update_layout(title_text="Process", font_size=10)
    fig.write_image("hoge.png")

if __name__ =="__main__":
    main()
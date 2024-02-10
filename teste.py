import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Estilos
estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", dbc.themes.LUX]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"

# Configuração do aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css])

app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server

# ========= Styles ========= #
card_style={'height': '100%',  'margin-bottom': '12px'}
tab_card = {'height': '100%'}

main_config = {
    "hovermode": "x unified",
    "legend": {"yanchor":"top", 
                "y":0.9, 
                "xanchor":"left",
                "x":0.1,
                "title": {"text": None},
                "font" :{"color":"white"},
                "bgcolor": "rgba(0,0,0,0.5)"},
    "margin": {"l":10, "r":10, "t":10, "b":10}
}

config_graph={"displayModeBar": False, "showTips": False}

# ===== Reading n cleaning File loja1 ====== #
df = pd.read_csv("lojas_01.2024.csv", sep=",")

df['data'] = pd.to_datetime(df['data'], format='%d-%m-%Y')


# To dict - para salvar no dcc.store

df_loja = df.to_dict()


sidebar_layout = dbc.Container([

     dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("TAB CELL",  style={'color': 'yellow'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
             html.H5("By VW CONTABILIDADE", style={'color': 'white'})
        ])
    ])
], style={'padding-top': '50px', 'margin-bottom': '100px'}, className='text-center'),
html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Nav([

                    dbc.NavItem(dbc.NavLink([html.I(className='fa fa-database dbc'), "\tPainel Geral"], href="/painel", active=True, style={'text-align': 'center'})),
                    
                    dbc.NavItem(html.Br()),

                    dbc.NavItem(dbc.NavLink([html.I(className='fa fa-comments dbc'), "\tComentários do Contador"], href="/contador", active=True, style={'text-align': 'center'})),

                   
                                    
                ],vertical="lg", pills=True, fill=True)
            ])
        ]),
        
], style={'height': '100vh', 'padding': '0px', 'position':'sticky', 'top': 0, 'background-color': '#232423'})

# Conteúdo Painel Geral
painel_layout = dbc.Container([
   
    dcc.Store(id='dataset', data=df_loja),
 
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Faturamento Total em 01/2024 (somatório de faturamento das lojas)", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph1', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, lg=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Custo Total em 01/2024(somatório do custo em cada loja)", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph2', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Faturamento total por dia em 01/2024 (faturamento de todas as lojas)", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph3', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Participação Percentual no Faturamento Total por Loja", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph4', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Lucro total por Dia em 01/2024", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph5', className='dbc card_padrao', config=config_graph)
                        ], sm=12, lg=12),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=8),
    ], className='g-2 my-auto', style={'margin-top': '7px', 'height': '100vh'})
], className='p-0', fluid=True, style={'height': '100vh'})


# Conteudo comentários do contador
contador_layout = dbc.Row([
    dbc.Col([
        html.H1("Perguntas e Comentários do Contador Consultor",style={'margin-bottom': '20px'}),


        html.H3("1. Comparativos de faturamento 12/2023 e 01/2024.", style={'margin-bottom': '5px'}),
        html.H5("R. Em 12/2023 a Loja 1 faturou R$ 10.769,00. Em 01/2024, por sua vez, o faturamento foi de R$ 13.900,00. Em termos percentuais, a loja 1 faturou 29% a mais do que o mês anterior.R. Em 12/2023 a Loja 2 faturou R$ 9.012,00. Em 01/2024, por sua vez, o faturamento foi de R$ 10.138,00. Em termos percentuais, a loja 2 faturou 12,49% a mais do que o mês anterior.R. Em 12/2023 a Loja 3 faturou R$ 7.001,00. Em 01/2024, por sua vez, o faturamento foi de R$ 10.345,00. Em termos percentuais, a loja 3 faturou 47,76%  a mais do que o mês anterior. Faturamento Total em 12/2023: R$ 26.782,00. Faturamento Total em 01/2024: R$ 34.383,00. Em 01/2024, o Faturamento Total teve um crescimento de 77,89%.",
                style={'margin-bottom': '30px'}),
        
        html.Br(),
        html.H3("2. Considerações sobre os custos da LOJA 2?", style={'margin-bottom': '5px'}),
        html.H5("R. Em 12/2023, a Loja 2 teve um custo de R$ 1.917,00. Em 01/2024, por sua vez, a Loja 2 teve um custo de R$ 1.875,50. Em termos percentuais, a Loja 02 diminuiu o seu custo em 3%.", 
                style={'margin-bottom': '30px'}),
        
        html.Br(),
        html.H3("3. Comparação Loja 2 e Loja 3!", style={'margin-bottom': '5px'}),
        html.H5("R. A Loja 3, quando comparada com a Loja 2, em 01/2024, apresentou um faturamento de R$ 10.345,00. A Loja 2, por sua vez, apresentou um faturamento de R$ 10.138,00. Nesse sentido, portanto, ao contrário do mês 12/2023, a Loja 3 conseguiu superar o faturamento da Loja 2.", 
                style={'margin-bottom': '30px'}),

        html.Br(),
        html.H3("*Observação:*. Espero que esse relatório seja capaz de fornecer informações relavantes sobre todas as variáveis que compõem o seu negócio. Além disso, esse relatório está na fase Beta e o esperado é que, com o passar do tempo, ele fique mais sofisticado e eficiente em termos de informação. Dito isso, obrigado pela parceria e confiança.", style={'margin-bottom': '5px'}),
        
        
    ])
])


# Layout principal
app.layout = dbc.Container([
    dcc.Location(id="url"),
    dcc.Store(id='data', data=df_loja),
    
    dbc.Row([
        dbc.Col([
            sidebar_layout
        ], md=2, style={'padding': '0px'}),

        dbc.Col([
            dbc.Container(id="page-content", fluid=True,style={'height': '100%', 'width': '100%', 'padding-left': '14px', 'min-height': '100vh'})
        ], md=10, style={'padding': '0px'})
    ], style={'height': '100vh'})
], fluid=True)


# Callbacks para atualizar o conteúdo da página
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):


    
    if pathname == "/" or pathname == "/painel":
        return painel_layout
    
    if pathname == "/contador":
        return contador_layout







# callback graph1 #
@app.callback(
    Output('graph1', 'figure'),
    Input('dataset', 'data'), 
    
)
def fat_dia(data):

     df = pd.DataFrame(df_loja)
     df_dia = df.groupby('loja')['faturamento_total'].sum().reset_index()

     # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
     df_dia['faturamento_formatado'] = 'R$ ' + df_dia['faturamento_total'].astype(str)

     fig1 = go.Figure(go.Bar(x=df_dia['loja'], y=df_dia['faturamento_total'], textposition='auto', text=df_dia['faturamento_formatado'], marker=dict(color='#404040')))

     fig1.update_layout(main_config, height=450, plot_bgcolor='white')

     fig1.update_xaxes(showgrid=False)

     fig1.update_yaxes(showgrid=False)


     return fig1




# callback graph2 #
@app.callback(
    Output('graph2', 'figure'),
    Input('dataset', 'data'), 
    
)
def fat_dia(data):

     df = pd.DataFrame(df_loja)
     df_dia = df.groupby('loja')['custo'].sum().reset_index()

     # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
     df_dia['custo_formatado'] = 'R$ ' + df_dia['custo'].astype(str)

     fig2 = go.Figure(go.Bar(y=df_dia['loja'], x=df_dia['custo'], textposition='auto', text=df_dia['custo_formatado'], marker=dict(color='#404040'), orientation='h'))

     fig2.update_layout(main_config, height=450, plot_bgcolor='white')

     fig2.update_xaxes(showgrid=False)

     fig2.update_yaxes(showgrid=False)


     return fig2





# callback graph3 #
@app.callback(
    Output('graph3', 'figure'),
    Input('dataset', 'data'),
)
def lucro(data):

    df = pd.DataFrame(df_loja)
    df_fat = df.groupby('data')['faturamento_total'].sum().reset_index()

    # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
    df_fat['lucro_formatado'] = 'R$ ' + df_fat['faturamento_total'].astype(str)

    fig3 = go.Figure(go.Scatter(
        x=df_fat['data'],
        y=df_fat['faturamento_total'],
        mode='lines',
        fill='tonexty',
        hovertemplate='<b>Data:</b> %{x}' +
                      '<br><b>faturamento_total:</b> %{text}<extra></extra>',
        text=df_fat['lucro_formatado'],
        marker=dict(color='#404040')
    ))
    
    fig3.add_annotation(text='faturamento_total',
        xref="paper", yref="paper",
        font=dict(
            size=17,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.85, showarrow=False)
    
    fig3.add_annotation(text=f"Média : {round(df_fat['faturamento_total'].mean(), 2)}",
        xref="paper", yref="paper",
        font=dict(
            size=20,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.55, showarrow=False)

    fig3.update_layout(main_config, height=540, plot_bgcolor='white')
    fig3.update_xaxes(showgrid=False, categoryorder='category ascending', title_text='DIAS', tickangle=45)
    fig3.update_yaxes(showgrid=False)
    
    return fig3



#GRAPH4
@app.callback(
    Output('graph4', 'figure'),
    Input('dataset', 'data'), 
)
def fat_smart(data):

    dff = pd.DataFrame(df_loja)
    df_smart = dff.groupby('loja')['faturamento_total'].sum().reset_index()

    # Defina as cores desejadas
    cores = ['#404040', '#FFD700']  # Cinza escuro e amarelo


    fig4 = go.Figure()
    fig4.add_trace(go.Pie(labels=df_smart['loja'], values=df_smart['faturamento_total'], hole=.7, marker=dict(colors=cores)))

    fig4.update_layout(main_config, height=450, plot_bgcolor='white')

    fig4.update_xaxes(showgrid=False)
    fig4.update_yaxes(showgrid=False)


    return fig4





#GRAPH5
@app.callback(
    Output('graph5', 'figure'),
    Input('dataset', 'data'),
)
def lucro(data):

    df = pd.DataFrame(df_loja)
    df_fat = df.groupby('data')['lucro'].sum().reset_index()

    # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
    df_fat['lucro_formatado'] = 'R$ ' + df_fat['lucro'].astype(str)

    fig5 = go.Figure(go.Scatter(
        x=df_fat['data'],
        y=df_fat['lucro'],
        mode='lines',
        fill='tonexty',
        hovertemplate='<b>Data:</b> %{x}' +
                      '<br><b>lucro:</b> %{text}<extra></extra>',
        text=df_fat['lucro_formatado'],
        marker=dict(color='#404040')
    ))
    
    fig5.add_annotation(text='lucro',
        xref="paper", yref="paper",
        font=dict(
            size=17,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.85, showarrow=False)
    
    fig5.add_annotation(text=f"Média : {round(df_fat['lucro'].mean(), 2)}",
        xref="paper", yref="paper",
        font=dict(
            size=20,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.55, showarrow=False)

    fig5.update_layout(main_config, height=450, plot_bgcolor='white')
    fig5.update_xaxes(showgrid=False, categoryorder='category ascending', title_text='DIAS', tickangle=45)
    fig5.update_yaxes(showgrid=False)
    
    return fig5






















if __name__ == '__main__':
    app.run_server(debug=True, port="8052")

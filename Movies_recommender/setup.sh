mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $Port\n\
enableCors =false\n\
headless =true\n\
\n\
" > ~/.streamlit/config.toml
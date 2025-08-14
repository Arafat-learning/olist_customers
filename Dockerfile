FROM jupyter/minimal-notebook

RUN pip install --no-cache-dir \
    polars \ 
    catppuccin-jupyterlab \
    seaborn

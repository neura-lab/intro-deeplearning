FROM tensorflow/tensorflow:1.0.0

RUN pip install plotly
RUN pip install phi
RUN pip install sympy
RUN pip install tflearn
RUN pip install coconut-develop

WORKDIR /notebooks

CMD coconut-develop --jupyter notebook

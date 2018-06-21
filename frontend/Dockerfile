# Angular Build
FROM mhart/alpine-node

WORKDIR /src/
COPY . /src/

RUN cd /src && npm install

CMD [ "npm", "start" ]

EXPOSE 4200 49153

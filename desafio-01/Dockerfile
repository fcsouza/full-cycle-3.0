FROM golang as build

WORKDIR /tmp/app
COPY main.go /tmp/app
RUN go build -o fullcycle

FROM alpine:3.7

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY --from=build /tmp/app/fullcycle /opt/app
CMD ["./fullcycle"]

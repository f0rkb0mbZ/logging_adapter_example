FROM gradle:latest

WORKDIR /app

COPY . .

RUN gradle bootJar

FROM eclipse-temurin:17

WORKDIR /app

COPY --from=0 /app/build/libs/demo-0.0.1-SNAPSHOT.jar .

CMD ["java", "-jar", "demo-0.0.1-SNAPSHOT.jar"]

EXPOSE 8080
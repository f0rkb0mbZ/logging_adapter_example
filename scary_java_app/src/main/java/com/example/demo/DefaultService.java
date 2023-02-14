package com.example.demo;

import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.util.Random;

@Slf4j
@Service
@EnableScheduling
public class DefaultService {

    @Scheduled(fixedDelay = 15 * 1000)
    public void logInfos() {
        Random random = new Random();
        int randomId = random.nextInt(Integer.MAX_VALUE);
        log.info("Processing request with ID " + randomId);
        log.info("Request with ID {} processed successfully in {} seconds", randomId, random.nextDouble(5));
    }

    @Scheduled(fixedDelay = 5 * 1000)
    public void logWarnErrs() {
        log.warn("Unable to connect to database at jdbc:mysql://localhost:3306/newdb, retrying in 5 seconds...");
        log.error("Failed to connect to database after 3 attempts");
    }
}

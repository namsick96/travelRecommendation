package com.travelrecommendation.travel.controller;

import com.travelrecommendation.travel.dto.FinalResult;
import com.travelrecommendation.travel.dto.TypeResult;
import com.travelrecommendation.travel.dto.UserFinalRequest;
import com.travelrecommendation.travel.service.ModelRequest;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.ArrayList;

@RestController
@RequestMapping("/final_result")
public class FinalResultController {

    @GetMapping
    public FinalResult final_result(@RequestBody UserFinalRequest request) throws IOException, InterruptedException {
        ModelRequest modelRequest = new ModelRequest();
        ArrayList<String> answer= modelRequest.startModel(request);
        FinalResult finalResult = new FinalResult();
        finalResult.setRoad(answer);
        return finalResult;
    }
}

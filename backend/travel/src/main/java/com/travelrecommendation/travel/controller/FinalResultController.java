package com.travelrecommendation.travel.controller;

import com.travelrecommendation.travel.dto.FinalResult;
import com.travelrecommendation.travel.dto.TypeResult;
import com.travelrecommendation.travel.dto.UserFinalRequest;
import com.travelrecommendation.travel.dto.UserFinalResponse;
import com.travelrecommendation.travel.service.ModelRequest;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.ArrayList;

@RestController
@CrossOrigin("*")
@RequestMapping("/final_result")
public class FinalResultController {

    @PostMapping
    public UserFinalResponse final_result(@RequestBody UserFinalRequest request) throws IOException, InterruptedException {
        ModelRequest modelRequest = new ModelRequest();
        return modelRequest.startModel(request);
    }
}

package com.travelrecommendation.travel.controller;

import com.travelrecommendation.travel.dto.TypeResult;
import com.travelrecommendation.travel.dto.UserFinalRequest;
import com.travelrecommendation.travel.dto.UserTestResultRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;

@Slf4j
@RestController
@RequestMapping("/test_result")
public class TestResultController {

    @GetMapping
    public TypeResult test_Result(@RequestBody UserTestResultRequest request){
//        Integer mukVal=request.getQ1().get("muk").getAsInt();

        //initialization
        HashMap<String,Integer> scores=new HashMap<>();
        scores.put("muk",0);
        scores.put("hansarang",0);
        scores.put("photo",0);
        scores.put("old",0);
        scores.put("healing",0);
        scores.put("activity",0);

        Integer mukVal=request.getQ1().get("muk");
        Integer travleVal=request.getQ2().get("travel");
        log.info(mukVal.toString());
        log.info(travleVal.toString());

        TypeResult type= new TypeResult();
        type.setType("muk");
        return type;

    }


}

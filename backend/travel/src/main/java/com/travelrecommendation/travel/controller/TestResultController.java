package com.travelrecommendation.travel.controller;

import com.travelrecommendation.travel.dto.TypeResult;
import com.travelrecommendation.travel.dto.UserFinalRequest;
import com.travelrecommendation.travel.dto.UserTestResultRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.lang.reflect.Field;
import java.util.HashMap;
import java.util.Set;

@Slf4j
@RestController
@RequestMapping("/test_result")
public class TestResultController {

    @GetMapping
    public TypeResult test_Result(@RequestBody UserTestResultRequest request) throws IllegalAccessException {
//        Integer mukVal=request.getQ1().get("muk").getAsInt();

        //initialization
        HashMap<String,Integer> scores=new HashMap<>();
        scores.put("muk",0);
        scores.put("hansarang",0);
        scores.put("photo",0);
        scores.put("old",0);
        scores.put("healing",0);
        scores.put("activity",0);

        log.info("test_result bean activated");

        for( HashMap<String,Integer> i : request.getAnswer()){
            Set<String> keySet=i.keySet();
            for(String key : keySet){
                scores.put(key,scores.get(key)+i.get(key));
            }
        }

        int maximum=-100000;
        String biggest="";
        Set<String> keySet=scores.keySet();
        for(String key : keySet){
            int now = scores.get(key);
            if(now>=maximum){
                biggest=key;
                maximum=now;
            }
        }
        TypeResult type= new TypeResult();
        type.setType(biggest);
        return type;

    }


}

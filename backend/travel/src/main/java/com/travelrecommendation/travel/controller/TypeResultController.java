package com.travelrecommendation.travel.controller;

import com.travelrecommendation.travel.dto.TypeResult;
import com.travelrecommendation.travel.dto.UserTypeResultRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@Slf4j
@RestController
@CrossOrigin("*")
@RequestMapping("/type_result")
public class TypeResultController {

    @PostMapping
    public TypeResult test_Result(@RequestBody UserTypeResultRequest request) throws IllegalAccessException {

        //initialization
        HashMap<String,Double> scores=new HashMap<>();
        scores.put("activity",0.0);
        scores.put("inside",0.0);
        scores.put("nature",0.0);
        scores.put("photo",0.0);
        scores.put("cafe",0.0);

//        log.info("test_result bean activated");

        for( HashMap<String,Double> i : request.getAnswer()){
            Set<String> keySet=i.keySet();
            for(String key : keySet){
                scores.put(key,scores.get(key)+i.get(key));
//                log.info(key);
            }
        }

//        log.info("test result bean activated2");


        double maximum=-100000;
        String biggest="";
        Set<String> keySet=scores.keySet();
        for(String key : keySet){
            double now = scores.get(key);
            if(now>=maximum){
                biggest=key;
                maximum=now;
            }
        }

        Integer biggestType=-1;
        if (biggest.equals("activity")){
            if(scores.get("cafe")>scores.get("photo") && scores.get("cafe")>scores.get("nature")){
                biggestType=5;
            }
            if(scores.get("nature")>scores.get("photo") && scores.get("nature")>scores.get("cafe")){
                biggestType=3;
            }
            else{
                biggestType=1;
            }

        }
        else if (biggest.equals("inside")){
            biggestType=7;
        }
        else if (biggest.equals("nature")){
            biggestType=6;
        }
        else if (biggest.equals("photo")){
            biggestType=4;
        }
        else if (biggest.equals("cafe")){
            biggestType=2;
        }


        TypeResult type= new TypeResult();
        type.setType(biggestType);
        type.setScores(scores);
        return type;

    }


}

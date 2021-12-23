package com.travelrecommendation.travel.controller;

import com.travelrecommendation.travel.dto.TypeResult;
import com.travelrecommendation.travel.dto.UserTypeResultRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Set;

@Slf4j
@RestController
@CrossOrigin("*")
@RequestMapping("/type_result")
public class TypeResultController {

    @PostMapping
    public TypeResult test_Result(@RequestBody UserTypeResultRequest request) throws IllegalAccessException {
//        Integer mukVal=request.getQ1().get("muk").getAsInt();

        //initialization
        HashMap<String,Integer> scores=new HashMap<>();
        scores.put("muk",0);
        scores.put("hansarang",0);
        scores.put("photo",0);
        scores.put("old",0);
        scores.put("healing",0);
        scores.put("activity",0);

//        log.info("test_result bean activated");

        for( HashMap<String,Integer> i : request.getAnswer()){
            Set<String> keySet=i.keySet();
            for(String key : keySet){
                scores.put(key,scores.get(key)+i.get(key));
//                log.info(key);
            }
        }

//        log.info("test result bean activated2");

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

//        log.info("test result bean activated3");

        TypeResult type= new TypeResult();
        type.setType(biggest);
        return type;

    }


}

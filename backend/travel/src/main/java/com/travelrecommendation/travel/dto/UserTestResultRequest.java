package com.travelrecommendation.travel.dto;


import com.fasterxml.jackson.databind.util.JSONWrappedObject;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;

@Getter
@Setter
public class UserTestResultRequest {

    private HashMap<String,Integer> q1;
    private HashMap<String,Integer> q2;
    private HashMap<String,Integer> q3;
    private HashMap<String,Integer> q4;
    private HashMap<String,Integer> q5;
    private HashMap<String,Integer> q6;
    private HashMap<String,Integer> q7;
    private HashMap<String,Integer> q8;
    private HashMap<String,Integer> q9;
    private HashMap<String,Integer> q10;
    private HashMap<String,Integer> q11;
    private HashMap<String,Integer> q12;

}

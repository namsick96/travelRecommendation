package com.travelrecommendation.travel.dto;


import com.fasterxml.jackson.databind.util.JSONWrappedObject;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

@Getter
@Setter
public class UserTestResultRequest {

    private List<HashMap<String,Integer>> answer;

}

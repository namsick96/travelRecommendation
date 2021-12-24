package com.travelrecommendation.travel.dto;


import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;
import java.util.List;

@Getter
@Setter
public class UserFinalResponse {
    private Integer type;
    private HashMap<String,List<String>> result;
}

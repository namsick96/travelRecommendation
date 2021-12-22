package com.travelrecommendation.travel.dto;


import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;
import java.util.List;

@Getter
@Setter
public class UserFinalRequest {
    private String type;
    private HashMap<String,Float> starting;
    private HashMap<String,Float> destination;
    private int mvp;
    private int first;
    private int second;
    private int third;
}

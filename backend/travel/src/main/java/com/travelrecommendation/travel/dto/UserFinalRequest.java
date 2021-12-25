package com.travelrecommendation.travel.dto;


import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;
import java.util.List;

@Getter
@Setter
public class UserFinalRequest {
    private Integer type;
    private HashMap<String,Float> starting;
    private HashMap<String,Float> destination;
    private HashMap<String,Double> scores;
    private Integer mvp;
    private String first;
    private String second;
    private String third;
    private String restaurant1;
    private String restaurant2;
    private String restaurant3;
    private String alchol1;
    private String alchol2;
    private String alchol3;
}

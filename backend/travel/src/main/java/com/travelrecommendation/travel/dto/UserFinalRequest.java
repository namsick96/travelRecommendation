package com.travelrecommendation.travel.dto;


import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;
import java.util.List;

@Getter
@Setter
public class UserFinalRequest {
    private int type;
    private HashMap<String,Float> starting;
    private HashMap<String,Float> destination;
    private int mvp;
    private String first;
    private String second;
    private String third;
}

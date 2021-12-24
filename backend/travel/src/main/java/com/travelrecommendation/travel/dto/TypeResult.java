package com.travelrecommendation.travel.dto;


import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;

@Getter
@Setter
public class TypeResult {

    private Integer type;
    private HashMap<String,Double> scores;
}

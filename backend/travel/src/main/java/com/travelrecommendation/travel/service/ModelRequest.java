package com.travelrecommendation.travel.service;

import com.travelrecommendation.travel.dto.UserFinalRequest;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class ModelRequest {
    public ArrayList<String> startModel(UserFinalRequest request) throws IOException, InterruptedException {

//        String command ="pwd";//"python3 /Users/jihoonan/Desktop/travelRecommendation/backend/test.py";
//        위에 command는 예시임.
        List<String> cmd= new ArrayList<>();
        cmd.add("python3");
        cmd.add("/Users/jihoonan/Desktop/travelRecommendation/backend/test.py");
        cmd.add(request.getType());
        ProcessBuilder builder=new ProcessBuilder(cmd);
        Process process=builder.start();
        InputStream input =process.getInputStream();

        int exitVal= process.waitFor();
        String text = new BufferedReader(
                new InputStreamReader(input, StandardCharsets.UTF_8))
                .lines()
                .collect(Collectors.joining("\n"));
        String []str=text.split(" ");
        ArrayList<String> tokens=new ArrayList<>();
        for (int i=0; i<str.length; i++){
            tokens.add(str[i]);
        }

        return tokens;
    }

}

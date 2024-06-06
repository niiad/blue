package com.niiad.blueProductService.util;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class Error {
    private static final long serialVersionUID = 1L;
    private String errorCode;
    private String message;
    private Integer status;
    private String url = "Not available";
    private String requestMethod = "Not available";
}

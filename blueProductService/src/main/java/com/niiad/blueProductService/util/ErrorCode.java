package com.niiad.blueProductService.util;

import lombok.AllArgsConstructor;
import lombok.Getter;

@AllArgsConstructor
@Getter
public enum ErrorCode {
    GENERIC_ERROR("GEN", "Unable to complete the request. Contact System Support"),
    HTTP_MEDIA_TYPE_NOT_SUPPORTED("MED", "Media type not supported. Use application/json"),
    HTTP_MESSAGE_NOT_WRITABLE("WRI", "Missing 'Accept' header"),
    HTTP_MEDIA_TYPE_NOT_ACCEPTABLE("ACC", "'Accept' header value not supported"),
    JSON_PARSE_ERROR("JSN", "Invalid JSON format"),
    HTTP_MESSAGE_NOT_READABLE("RED", "Invalid request payload");


    private final String code;
    private final String messageKey;
}

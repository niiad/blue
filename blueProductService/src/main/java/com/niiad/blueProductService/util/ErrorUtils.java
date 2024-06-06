package com.niiad.blueProductService.util;

public class ErrorUtils {
    private ErrorUtils() {}

    public static Error createError(final String messageKey, final String code, final Integer httpStatusCode) {
        Error error = new Error();

        error.setErrorCode(code);
        error.setMessage(messageKey);
        error.setStatus(httpStatusCode);

        return error;
    }
}

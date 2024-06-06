package com.niiad.blueProductService.util;

import com.fasterxml.jackson.core.JsonParseException;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.http.converter.HttpMessageNotWritableException;
import org.springframework.web.HttpMediaTypeNotAcceptableException;
import org.springframework.web.HttpMediaTypeNotSupportedException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import java.util.Locale;

@ControllerAdvice
public class RestApiErrorHandler {
    private final MessageSource messageSource;

    @Autowired
    public RestApiErrorHandler(MessageSource messageSource) {
        this.messageSource = messageSource;
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<Error> handleException(HttpServletRequest request, Exception exception, Locale locale) {
        Error error = ErrorUtils
                .createError(ErrorCode.GENERIC_ERROR.getMessageKey(), ErrorCode.GENERIC_ERROR.getCode(), HttpStatus.INTERNAL_SERVER_ERROR.value());

        error.setRequestMethod(request.getMethod());
        error.setUrl(request.getRequestURI());

        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @ExceptionHandler(HttpMediaTypeNotAcceptableException.class)
    public ResponseEntity<Error> handleHttpMediaTypeNotSupportedException(HttpServletRequest request, HttpMediaTypeNotSupportedException exception, Locale locale) {
        Error error = ErrorUtils
                .createError(ErrorCode.HTTP_MEDIA_TYPE_NOT_SUPPORTED.getMessageKey(), ErrorCode.HTTP_MEDIA_TYPE_NOT_SUPPORTED.getCode(), HttpStatus.UNSUPPORTED_MEDIA_TYPE.value());

        error.setUrl(request.getRequestURL().toString());
        error.setRequestMethod(request.getMethod());

        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @ExceptionHandler(HttpMessageNotWritableException.class)
    public ResponseEntity<Error> handleHttpMessageNotWritableException(HttpServletRequest request, HttpMessageNotWritableException exception, Locale locale) {
        Error error = ErrorUtils
                .createError(ErrorCode.HTTP_MESSAGE_NOT_WRITABLE.getMessageKey(), ErrorCode.HTTP_MESSAGE_NOT_WRITABLE.getCode(), HttpStatus.UNSUPPORTED_MEDIA_TYPE.value());

        error.setUrl(request.getRequestURL().toString());
        error.setRequestMethod(request.getMethod());

        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @ExceptionHandler(HttpMediaTypeNotAcceptableException.class)
    public ResponseEntity<Error> handleHttpMediaTypeNotAcceptableException(HttpServletRequest request, HttpMediaTypeNotAcceptableException exception, Locale locale) {
        Error error = ErrorUtils
                .createError(ErrorCode.HTTP_MEDIA_TYPE_NOT_ACCEPTABLE.getMessageKey(), ErrorCode.HTTP_MEDIA_TYPE_NOT_ACCEPTABLE.getCode(), HttpStatus.UNSUPPORTED_MEDIA_TYPE.value());

        error.setUrl(request.getRequestURL().toString());
        error.setRequestMethod(request.getMethod());

        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Error> handleHttpMessageNotReadableException(HttpServletRequest request, HttpMessageNotReadableException exception, Locale locale) {
        Error error = ErrorUtils
                .createError(ErrorCode.HTTP_MESSAGE_NOT_READABLE.getMessageKey(), ErrorCode.HTTP_MESSAGE_NOT_READABLE.getCode(), HttpStatus.NOT_ACCEPTABLE.value());

        error.setUrl(request.getRequestURL().toString());
        error.setRequestMethod(request.getMethod());

        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @ExceptionHandler(JsonParseException.class)
    public ResponseEntity<Error> handleJsonParseException(HttpServletRequest request, JsonParseException exception, Locale locale) {
        Error error = ErrorUtils
                .createError(ErrorCode.JSON_PARSE_ERROR.getMessageKey(), ErrorCode.JSON_PARSE_ERROR.getCode(), HttpStatus.NOT_ACCEPTABLE.value());

        error.setUrl(request.getRequestURL().toString());
        error.setRequestMethod(request.getMethod());

        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}

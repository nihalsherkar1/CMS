package com.cms.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin("*")
@RestController
@RequestMapping("/cms/auth")
public class AuthController {

	@GetMapping("/login")
	public String login() {
		System.out.println("Login request is working....");
		return "Login is working";
	}
}

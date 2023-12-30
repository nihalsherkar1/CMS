package com.cms.services;

import java.sql.Blob;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cms.entities.Users;
import com.cms.repository.UserRepository;

@Service
public class UserServiceImpl implements UserServices {
	
	@Autowired
	private UserRepository userRepository;

	@Override
	public Users addUser(Users user) {
		return userRepository.save(user);
	}

	public boolean validateLogin(String email,String password) {
		 Users user=userRepository.findByEmail(email);
		 return user != null && user.getPassword().equals(password);
	}
	
	public boolean  validatePassword(String password) {
		Users user=userRepository.findByPassword(password);
		return user !=null && user.getPassword().equals(password);
	}
	
	public byte[] getUserImage(Long id) {
		// Return an empty byte array if the image is null
		return userRepository.findImageById(id) ;
	}
}

package com.cms.dao;

import org.springframework.data.jpa.repository.JpaRepository;

import com.cms.models.User;

public interface UserDao extends JpaRepository<User, Long> {
	
	public User findByEmail(String email);
}

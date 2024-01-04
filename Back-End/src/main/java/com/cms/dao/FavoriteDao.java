package com.cms.dao;

import org.springframework.data.jpa.repository.JpaRepository;

import com.cms.models.Favourite;


public interface FavoriteDao extends JpaRepository<Favourite, Long> {

}

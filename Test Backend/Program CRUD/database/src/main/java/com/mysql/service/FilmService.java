package com.mysql.service;

import com.mysql.model.Film;
import java.util.List;

public interface FilmService {
    Film updateFilmById(Long id, Film film);
    // Mungkin ada metode lainnya di sini

    Film saveFilm(Film film);

    Film getFilmById(Long id);

    List<Film> fetchFilmList();

    void deleteFilmById(Long id);
}

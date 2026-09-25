// Archivo: core/frontend/lib/ui/temas/tema_ide.dart
import 'package:flutter/material.dart';

/// Tema base del IDE con identidad visual corporativa (Azul Oscuro / Verde).
class TemaIde {
  static const Color colorPrimario = Color(0xFF1B3A5C);
  static const Color colorSecundario = Color(0xFF008A00);
  static const Color colorFondo = Color(0xFFF5F5F5);
  static const Color colorConsola = Color(0xFF1E1E1E);
  static const Color colorTextoConsola = Color(0xFF8DC63F);

  static ThemeData claro() => ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: colorPrimario,
          primary: colorPrimario,
          secondary: colorSecundario,
          surface: colorFondo,
        ),
        useMaterial3: true,
        scaffoldBackgroundColor: colorFondo,
        appBarTheme: const AppBarTheme(
          backgroundColor: colorPrimario,
          foregroundColor: Colors.white,
          elevation: 0,
        ),
      );

  static ThemeData oscuro() => ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: colorPrimario,
          brightness: Brightness.dark,
          primary: colorPrimario,
          secondary: colorSecundario,
        ),
        useMaterial3: true,
        appBarTheme: const AppBarTheme(
          backgroundColor: colorPrimario,
          foregroundColor: Colors.white,
          elevation: 0,
        ),
      );
}

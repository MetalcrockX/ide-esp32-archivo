// Archivo: core/frontend/lib/ui/layout/layout_principal.dart
import 'package:flutter/material.dart';

import '../../nucleo/registro_modulos.dart';
import '../temas/tema_ide.dart';

/// Layout maestro rediseñado del IDE para escritorio (Estilo Arduino/VSCode).
class LayoutPrincipal extends StatefulWidget {
  const LayoutPrincipal({
    super.key,
    required this.registro,
    this.titulo = 'IDE ESP32-S31 — Sketch sin título',
  });

  final RegistroModulos registro;
  final String titulo;

  @override
  State<LayoutPrincipal> createState() => _LayoutPrincipalState();
}

class _LayoutPrincipalState extends State<LayoutPrincipal> {
  int _indiceModulo = 0;
  String _placaSeleccionada = 'ESP32-S31 Dev Module';
  String _puertoSeleccionado = 'COM3';
  String _estadoIde = 'Listo';

  final TextEditingController _codigoController = TextEditingController(
    text: 'void setup() {\n  Serial.begin(115200);\n}\n\nvoid loop() {\n  // código aquí\n}',
  );

  final List<String> _logsConsola = [
    'Salida:',
    'Compilando sketch...',
    'Cargando en ESP32-S31...',
    'Listo.',
  ];

  void _agregarLog(String mensaje) {
    setState(() {
      _logsConsola.add(mensaje);
      _estadoIde = mensaje.replaceAll('...', '').trim();
      if (_estadoIde.isEmpty) _estadoIde = 'Listo';
    });
  }

  @override
  Widget build(BuildContext context) {
    final modulos = widget.registro.modulos;
    final actual = modulos.isNotEmpty ? modulos[_indiceModulo] : null;

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.titulo, style: const TextStyle(fontSize: 16)),
        backgroundColor: TemaIde.colorPrimario,
        actions: [
          // Selector de Placa
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 8),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 8),
              decoration: BoxDecoration(
                color: Colors.white24,
                borderRadius: BorderRadius.circular(4),
              ),
              child: DropdownButton<String>(
                value: _placaSeleccionada,
                dropdownColor: TemaIde.colorPrimario,
                style: const TextStyle(color: Colors.white, fontSize: 13),
                underline: const SizedBox(),
                items: <String>[
                  'ESP32-S31 Dev Module',
                  'ESP32-S31 DevKit',
                  'ESP32-S31 WROOM',
                ].map<DropdownMenuItem<String>>((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (String? newValue) {
                  if (newValue != null) {
                    setState(() => _placaSeleccionada = newValue);
                    _agregarLog('Placa cambiada a: $newValue');
                  }
                },
              ),
            ),
          ),
          // Selector de Puerto
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 8),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 8),
              decoration: BoxDecoration(
                color: Colors.white24,
                borderRadius: BorderRadius.circular(4),
              ),
              child: DropdownButton<String>(
                value: _puertoSeleccionado,
                dropdownColor: TemaIde.colorPrimario,
                style: const TextStyle(color: Colors.white, fontSize: 13),
                underline: const SizedBox(),
                items: <String>['COM3', 'COM4', '/dev/ttyUSB0', '/dev/ttyACM0']
                    .map<DropdownMenuItem<String>>((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (String? newValue) {
                  if (newValue != null) {
                    setState(() => _puertoSeleccionado = newValue);
                    _agregarLog('Puerto seleccionado: $newValue');
                  }
                },
              ),
            ),
          ),
          // Boton Verificar (Compilar)
          IconButton(
            icon: const Icon(Icons.check_circle_outline, color: Colors.greenAccent),
            tooltip: 'Verificar / Compilar',
            onPressed: () {
              _agregarLog('Compilando...');
              Future.delayed(const Duration(seconds: 1), () {
                _agregarLog('Compilación exitosa.');
              });
            },
          ),
          // Boton Subir (Flash)
          IconButton(
            icon: const Icon(Icons.arrow_forward_ios, color: Colors.lightBlueAccent),
            tooltip: 'Subir firmware',
            onPressed: () {
              _agregarLog('Cargando en placa...');
              Future.delayed(const Duration(seconds: 1), () {
                _agregarLog('Listo.');
              });
            },
          ),
          const SizedBox(width: 8),
        ],
      ),
      body: Column(
        children: [
          // Barra de Menús estilo Desktop
          Container(
            color: Colors.grey.shade200,
            padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 2),
            child: Row(
              children: [
                _buildMenuButton('Archivo', ['Nuevo', 'Abrir', 'Guardar', 'Salir']),
                _buildMenuButton('Editar', ['Deshacer', 'Rehacer', 'Cortar', 'Copiar', 'Pegar']),
                _buildMenuButton('Sketch', ['Verificar / Compilar', 'Subir', 'Exportar binario']),
                _buildMenuButton('Herramientas', [
                  'Auto Formato',
                  'Monitor Serie',
                  'Información de la Placa',
                  'Recargar datos',
                ]),
                _buildMenuButton('Ayuda', ['Documentación', 'Acerca de']),
                const Spacer(),
                if (modulos.length > 1)
                  Padding(
                    padding: const EdgeInsets.only(right: 8),
                    child: DropdownButton<int>(
                      value: _indiceModulo,
                      isDense: true,
                      underline: const SizedBox(),
                      items: [
                        for (int i = 0; i < modulos.length; i++)
                          DropdownMenuItem(
                            value: i,
                            child: Text(
                              'Módulo: ${modulos[i].nombre}',
                              style: const TextStyle(fontSize: 12),
                            ),
                          ),
                      ],
                      onChanged: (i) => setState(() => _indiceModulo = i ?? 0),
                    ),
                  ),
              ],
            ),
          ),
          const Divider(height: 1),
          // Área principal: Editor y Consola
          Expanded(
            child: Row(
              children: [
                // Panel de Código y Consola
                Expanded(
                  flex: 3,
                  child: Column(
                    children: [
                      // Editor de Código
                      Expanded(
                        child: Container(
                          color: Colors.white,
                          child: Row(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              // Números de línea simulados
                              Container(
                                width: 40,
                                color: Colors.grey.shade100,
                                padding: const EdgeInsets.symmetric(vertical: 12),
                                child: Column(
                                  children: List.generate(
                                    15,
                                    (index) => Text(
                                      '${index + 1}',
                                      style: TextStyle(
                                        color: Colors.grey.shade500,
                                        fontSize: 12,
                                        fontFamily: 'monospace',
                                      ),
                                    ),
                                  ),
                                ),
                              ),
                              const VerticalDivider(width: 1),
                              // Campo de texto del editor
                              Expanded(
                                child: Padding(
                                  padding: const EdgeInsets.all(8.0),
                                  child: TextField(
                                    controller: _codigoController,
                                    maxLines: null,
                                    keyboardType: TextInputType.multiline,
                                    style: const TextStyle(
                                      fontFamily: 'monospace',
                                      fontSize: 14,
                                    ),
                                    decoration: const InputDecoration(
                                      border: InputBorder.none,
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      const Divider(height: 1),
                      // Consola de Salida
                      Container(
                        height: 160,
                        color: TemaIde.colorConsola,
                        padding: const EdgeInsets.all(8),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Row(
                              children: [
                                Text(
                                  'SALIDA DE CONSOLA',
                                  style: TextStyle(
                                    color: Colors.white70,
                                    fontSize: 11,
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 4),
                            Expanded(
                              child: ListView.builder(
                                itemCount: _logsConsola.length,
                                itemBuilder: (context, index) {
                                  return Text(
                                    _logsConsola[index],
                                    style: const TextStyle(
                                      color: TemaIde.colorTextoConsola,
                                      fontFamily: 'monospace',
                                      fontSize: 12,
                                    ),
                                  );
                                },
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
                // Si hay vista de módulo activa, la mostramos en un panel lateral o pestaña
                if (actual != null) ...[
                  const VerticalDivider(width: 1),
                  Expanded(
                    flex: 2,
                    child: Container(
                      color: Colors.white,
                      child: actual.construirVista(context),
                    ),
                  ),
                ],
              ],
            ),
          ),
          // Barra de Estado Inferior
          Container(
            color: TemaIde.colorPrimario,
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            child: Row(
              children: [
                Text(
                  _placaSeleccionada,
                  style: const TextStyle(color: Colors.white, fontSize: 12),
                ),
                const Text(' | ', style: TextStyle(color: Colors.white54)),
                Text(
                  _puertoSeleccionado,
                  style: const TextStyle(color: Colors.white, fontSize: 12),
                ),
                const Text(' | ', style: TextStyle(color: Colors.white54)),
                Expanded(
                  child: Text(
                    _estadoIde,
                    style: const TextStyle(color: Colors.greenAccent, fontSize: 12),
                  ),
                ),
                const Text(
                  'ESP32-S31 v1.0.0',
                  style: TextStyle(color: Colors.white54, fontSize: 12),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildMenuButton(String titulo, List<String> opciones) {
    return PopupMenuButton<String>(
      padding: EdgeInsets.zero,
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
        child: Text(titulo, style: const TextStyle(fontSize: 13, color: Colors.black87)),
      ),
      itemBuilder: (BuildContext context) {
        return opciones.map((String opcion) {
          return PopupMenuItem<String>(
            value: opcion,
            child: Text(opcion, style: const TextStyle(fontSize: 13)),
          );
        }).toList();
      },
      onSelected: (String valor) {
        _agregarLog('Menú [$titulo] -> $valor');
      },
    );
  }
}

import 'package:flutter_test/flutter_test.dart';
import 'package:ide_app/main.dart';
import 'package:ide_app/nucleo/registro_modulos.dart';
import 'package:ide_core/ide_core.dart';

void main() {
  testWidgets('IDE app smoke test', (WidgetTester tester) async {
    final registro = RegistroModulos(construirModulos());
    await tester.pumpWidget(IdeApp(registro: registro));

    expect(find.text('Herramientas'), findsWidgets);
  });
}

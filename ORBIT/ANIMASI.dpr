program ANIMASI;

uses
  Forms,
  ANIMASI1 in 'ANIMASI1.pas' {Form1};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.

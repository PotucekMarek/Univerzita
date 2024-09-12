using System;
using System.Collections.Generic;
using System.Windows;
using System.Windows.Input;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace Snake
{
    public partial class MainWindow : Window {
        int SIRKAPOLE = 530;
        int VYSKAPOLE = 640;
        int _smer = 0;
        int _skore = 0;
        int dolu = 1;
        int vlevo = 2;
        int vpravo = 3;
        int nahoru = 4;
        int _x = 10;
        int _y = 10;
        int _count = 0;
        DispatcherTimer timer;
        List<Had> teloHada;
        List<Jidlo> jidlo;
        readonly Random _rd = new Random();
        public MainWindow() {
            InitializeComponent();
            timer = new DispatcherTimer();
            timer.Interval = new TimeSpan(0, 0, 0, 0, 40); // změna rychlosti
            timer.Tick += Pohyb;
            teloHada = new List<Had>();
            teloHada.Add(new Had(_x, _y));
            jidlo = new List<Jidlo>();
            jidlo.Add(new Jidlo(_rd.Next(5, 20) * 10, _rd.Next(5, 20) * 10));
        }
        private void VykresliHadaDoCanvasu() {
            var index = 0;
            for (; index < teloHada.Count; index++) {
                var had = teloHada[index];
                had.HadovaPozice();
                Canvas.Children.Add(had.hlava);
            }
        }
        void Pohyb(object sender, EventArgs e) {
            if (_smer != 0) {
                int i;
                for (i = teloHada.Count - 1; i >= 1; i--) {
                    teloHada[index: i] = teloHada[index: i - 1];
                }
            }
            if (_smer == nahoru) _y -= 10;
            if (_smer == dolu) _y += 10;
            if (_smer == vlevo) _x -= 10;
            if (_smer == vpravo) _x += 10;
            if (teloHada[0].x == jidlo[0].x && teloHada[0].y == jidlo[0].y) {
                teloHada.Add(new Had(jidlo[0].x, jidlo[0].y));
                jidlo[0] = new Jidlo(_rd.Next(0, SIRKAPOLE/10) * 10, _rd.Next(0, VYSKAPOLE/10) * 10);
                Canvas.Children.RemoveAt(0);
                _skore++;
                SkoreCanvas.Text = _skore.ToString();
                VykresliMysDoCanvasu();
            }
            teloHada[0] = new Had(_x, _y);
            if (teloHada[0].x > SIRKAPOLE || teloHada[0].y > VYSKAPOLE || teloHada[0].x < 0 || teloHada[0].y < 0) this.Close();
            for (int i = 1; i < teloHada.Count; i++) 
                if (teloHada[0].x == teloHada[i].x && teloHada[0].y == teloHada[i].y) this.Close();
            for (int i = 0; i < Canvas.Children.Count; i++) 
                if (Canvas.Children[i] is Rectangle) _count++;
            Canvas.Children.RemoveRange(1, _count);
            _count = 0;
            VykresliHadaDoCanvasu();
        }

        private void VykresliMysDoCanvasu() {
            jidlo[0].MysiPozice();
            Canvas.Children.Insert(0, jidlo[0].mys);
        }
        private void WindowKeyDown(object sender, KeyEventArgs e) {
            if (e.Key == Key.Up && _smer != dolu) _smer = nahoru;
            if (e.Key == Key.Down && _smer != nahoru) _smer = dolu;
            if (e.Key == Key.Left && _smer != vpravo) _smer = vlevo;
            if (e.Key == Key.Right && _smer != vlevo) _smer = vpravo;
        }
        private void WindowLoaded(object sender, RoutedEventArgs e) {
            VykresliMysDoCanvasu();
            VykresliHadaDoCanvasu();
            timer.Start();
        }
    }
}

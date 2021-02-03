

    switch (message)
    {
    case WM_COMMAND:
        {
            int wmId = LOWORD(wParam);
            // 分析菜单选择:
            switch (wmId)
            {
            case IDM_ABOUT:
                DialogBox(hInst, MAKEINTRESOURCE(IDD_ABOUTBOX), hWnd, About);
                break;
            case IDM_EXIT:
                DestroyWindow(hWnd);
                break;
            default:
                return DefWindowProc(hWnd, message, wParam, lParam);
            }
        }
        break;
    case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hWnd, &ps);
            int RADIUS = 40;
            int DISTANCE = 10;
            double DEGREE = 3.1415926 / 180;
            int centerX = 300;
            int centerY = 200;
            SelectObject(hdc, GetStockObject(NULL_BRUSH));
            Ellipse(hdc, centerX - RADIUS, centerY - RADIUS, centerX + RADIUS, centerY + RADIUS);
            for (int lay = 1; lay < 3; lay = lay + 1);
            {
                for (int jj = 0; jj < 8 * lay; jj = jj + 1)
                {
                    double angle = 360.0 / 8 / lay;
                    int cX = centerX + (int)(lay * (2 * RADIUS - DISTANCE) * cos(jj * angle * DEGREE));
                    int cY = centerY + (int)(lay * (2 * RADIUS - DISTANCE) * sin(jj * angle * DEGREE));
                    Ellipse(hdc, cX - RADIUS, cY - RADIUS, cX + RADIUS, cY + RADIUS);
                }
            }
            HPEN OLDPEN = CreatePen(PS_DASHDOT, 1, RGB(122, 34, 99));
            HBRUSH yinyinghuabi = CreateHatchBrush(HS_CROSS, RGB(23, 43, 54));
            SelectObject(hdc, yinyinghuabi);
            TextOut(hdc, 500, 500, "Hello world!", lstrlen("Hello world!"));
            COLORREF Red = RGB(255, 0, 0), Green = RGB(0, 255, 0), Suiji = RGB(54, 68, 145);
            COLORREF RedBkcolor = RGB(255, 34, 34), GreenBkcolor = RGB(23, 255, 45);
            SetBkMode(hdc, TRANSPARENT);
            SetBkColor(hdc, GreenBkcolor);
            SetTextColor(hdc, Red);
            TextOut(hdc, 400, 400, "Hello world!", lstrlen("Hello world!"));
            MoveToEx(hdc, 10, 10, NULL);
            LineTo(hdc, 530, 530);
            Rectangle(hdc, 630, 230,700, 600);
            Ellipse(hdc, 10, 149, 400, 88);
            RoundRect(hdc, 10, 149, 400, 88, 25, 25);
            // TODO: 在此处添加使用 hdc 的任何绘图代码...
            EndPaint(hWnd, &ps);
        }
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;


// “关于”框的消息处理程序。


